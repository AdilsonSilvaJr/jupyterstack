#Libraries
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType,IntegerType,DoubleType,LongType

conf = (
SparkConf()
    .setAppName("Spark minIO")
    .set("spark.hadoop.fs.s3a.endpoint", "http://localhost:9001")
    .set("spark.hadoop.fs.s3a.access.key", "HJ740SV1UBDK4ZG8D7ZP")
    .set("spark.hadoop.fs.s3a.secret.key", "g++oLrfPYxcMY1rMkE36MP2k+yqPff9P+1wzS0dt")
    .set("spark.hadoop.fs.s3a.path.style.access", True)
    .set("spark.hadoop.fs.s3a.fast.upload", True)
    .set("spark.hadoop.fs.s3a.connection.maximun",100)         
    .set("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
)
sc = SparkContext(conf=conf).getOrCreate()

#Specify data type of dataframes
schema_df1 = StructType( \
                     [StructField("Diabetes_012", DoubleType(),True), \
                      StructField("HighBP", DoubleType(), True), \
                      StructField("HighChol", DoubleType(), True), \
                      StructField('CholCheck', DoubleType(), True), \
                      StructField("BMI", DoubleType(), True), \
                      StructField("Smoker", DoubleType(), True), \
                      StructField("Stroke", DoubleType(), True), \
                      StructField("HeartDiseaseorAttack", DoubleType(), True),\
                      StructField("PhysActivity", DoubleType(), True), \
                      StructField("Fruits", DoubleType(), True), \
                      StructField("Veggies", DoubleType(),True), \
                      StructField("HvyAlcoholConsump", DoubleType(), True), \
                      StructField("AnyHealthcare", DoubleType(), True), \
                      StructField("NoDocbcCost", DoubleType(), True), \
                      StructField("GenHlth", DoubleType(), True), \
                      StructField("MentHlth", DoubleType(),True), \
                      StructField("PhysHlth", DoubleType(), True), \
                      StructField("DiffWalk", DoubleType(), True), \
                      StructField("Sex", DoubleType(), True), \
                      StructField("Age", DoubleType(), True), \
                      StructField("Education", DoubleType(),True), \
                      StructField("Income", DoubleType(), True), \
                        ])
schema_df2 = StructType( \
                     [StructField("Diabetes_binary", DoubleType(),True), \
                      StructField("HighBP", DoubleType(), True), \
                      StructField("HighChol", DoubleType(), True), \
                      StructField('CholCheck', DoubleType(), True), \
                      StructField("BMI", DoubleType(), True), \
                      StructField("Smoker", DoubleType(), True), \
                      StructField("Stroke", DoubleType(), True), \
                      StructField("HeartDiseaseorAttack", DoubleType(), True),\
                      StructField("PhysActivity", DoubleType(), True), \
                      StructField("Fruits", DoubleType(), True), \
                      StructField("Veggies", DoubleType(),True), \
                      StructField("HvyAlcoholConsump", DoubleType(), True), \
                      StructField("AnyHealthcare", DoubleType(), True), \
                      StructField("NoDocbcCost", DoubleType(), True), \
                      StructField("GenHlth", DoubleType(), True), \
                      StructField("MentHlth", DoubleType(),True), \
                      StructField("PhysHlth", DoubleType(), True), \
                      StructField("DiffWalk", DoubleType(), True), \
                      StructField("Sex", DoubleType(), True), \
                      StructField("Age", DoubleType(), True), \
                      StructField("Education", DoubleType(),True), \
                      StructField("Income", DoubleType(), True), \
                        ])
schema_df3 = StructType( \
                     [StructField("Diabetes_binary", DoubleType(),True), \
                      StructField("HighBP", DoubleType(), True), \
                      StructField("HighChol", DoubleType(), True), \
                      StructField('CholCheck', DoubleType(), True), \
                      StructField("BMI", DoubleType(), True), \
                      StructField("Smoker", DoubleType(), True), \
                      StructField("Stroke", DoubleType(), True), \
                      StructField("HeartDiseaseorAttack", DoubleType(), True),\
                      StructField("PhysActivity", DoubleType(), True), \
                      StructField("Fruits", DoubleType(), True), \
                      StructField("Veggies", DoubleType(),True), \
                      StructField("HvyAlcoholConsump", DoubleType(), True), \
                      StructField("AnyHealthcare", DoubleType(), True), \
                      StructField("NoDocbcCost", DoubleType(), True), \
                      StructField("GenHlth", DoubleType(), True), \
                      StructField("MentHlth", DoubleType(),True), \
                      StructField("PhysHlth", DoubleType(), True), \
                      StructField("DiffWalk", DoubleType(), True), \
                      StructField("Sex", DoubleType(), True), \
                      StructField("Age", DoubleType(), True), \
                      StructField("Education", DoubleType(),True), \
                      StructField("Income", DoubleType(), True), \
                        ])

if __name__ == "__main__":
    spark = SparkSession.builder \
            .master("local") \
            .appName("parquet_diabetes") \
            .getOrCreate()

#Read dataframes
df1 = spark.read \
        .format("csv") \
        .option("header", "true") \
        .schema(schema_df1) \
        .csv("s3a://jupyter-diabetes/diabetes_012_health_indicators_BRFSS2015.csv")
        #.csv("dataset/diabetes_012_health_indicators_BRFSS2015.csv")


df1.show()

df2 = spark.read \
        .format("csv") \
        .option("header", "true") \
        .schema(schema_df2).load('dataset/diabetes_binary_5050split_health_indicators_BRFSS2015.csv')

df3 = spark.read \
        .format("csv") \
        .option("header", "true") \
        .schema(schema_df3).load('dataset/diabetes_binary_health_indicators_BRFSS2015.csv')

#Drop duplicate values on dataframes
df1 = df1.dropDuplicates()

df2 = df2.dropDuplicates()

df3 = df3.dropDuplicates()

#Export dataframes
# df1.write.mode('overwrite').parquet('tmp/diabetes_012_health_indicators_BRFSS2015.parquet')

# df2.write.mode('overwrite').parquet('tmp/diabetes_binary_5050split_health_indicators_BRFSS2015.parquet')

# df3.write.mode('overwrite').parquet('tmp/diabetes_binary_health_indicators_BRFSS2015.parquet')

# df1.write.mode('overwrite').parquet('s3a://jupyter-diabetes/diabetes_012_health_indicators_BRFSS2015.parquet')

# df2.write.mode('overwrite').parquet('s3a://jupyter-diabetes/diabetes_binary_5050split_health_indicators_BRFSS2015.parquet')

# df3.write.mode('overwrite').parquet('s3a://jupyter-diabetes/diabetes_binary_health_indicators_BRFSS2015.parquet')


# spark-submit /home/adilson/Documents/jupyterstack/server-jupyter/Ingest_diabetes_notebook.py

# spark-submit \
# --conf spark.hadoop.fs.s3a.endpoint=http://localhost:9001 \
# --conf spark.hadoop.fs.s3a.access.key=MOY1KKX03S9TTCB67PJ8 \
# --conf spark.hadoop.fs.s3a.secret.key=HiqieJmEYAISPg52m7hCRybwHMkm088+bXOPhdF1 \
# --conf spark.hadoop.fs.s3a.path.style.access=True \
# --conf spark.hadoop.fs.s3a.fast.upload=True \
# --conf spark.hadoop.fs.s3a.connection.maximun=100 \       
# --conf spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem \
# /home/adilson/Documents/jupyterstack/server-jupyter/Ingest_diabetes_notebook.py


# wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.2/hadoop-aws-3.3.2.jar

# wget https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk/1.7.4/aws-java-sdk-1.7.4.jar

# kubectl exec -ti --namespace default spark-worker-0 -- spark-submit --master spark://spark-master-svc:7077 \
# --class org.apache.spark.examples.SparkPi \
# --conf spark.kubernetes.executor.volumes.persistentVolumeClaim.spark-local-dir-1.options.claimName=OnDemand \
# --conf spark.kubernetes.executor.volumes.persistentVolumeClaim.spark-local-dir-1.options.storageClass=gp \
# --conf spark.kubernetes.executor.volumes.persistentVolumeClaim.spark-local-dir-1.options.sizeLimit=500Gi \
# --conf spark.kubernetes.executor.volumes.persistentVolumeClaim.spark-local-dir-1.mount.path=/home/adilson/Documents/jupyterstack/server-jupyter/ \
# --conf zspark.kubernetes.executor.volumes.persistentVolumeClaim.spark-local-dir-1.mount.readOnly=false \
# Ingest_diabetes_notebook.py

# ./bin/spark-submit \
#   --master k8s://$K8S_SERVER \
#   --deploy-mode cluster \
#   --name $POD_NAME \
#   --conf spark.kubernetes.container.image=spark:v3.2.1 \
#   --conf spark.kubernetes.driver.pod.name=$POD_NAME \
#   --conf spark.kubernetes.namespace=spark-demo \
#   --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark \
#   local:///home/adilson/Documents/jupyterstack/server-jupyter/Ingest_diabetes_notebook.py