"""val w = Window.orderBy($"SL_NO")
dataset.withColumn("AMOUNT",
         when($"ID" === lag($"ID", 1).over(w),
              lag($"AMOUNT", 1).over(w))\
              .otherwise($"AMOUNT")
).show"""