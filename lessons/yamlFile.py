
import yaml

# print(yaml.dump(open("test.yaml"), Loader=yaml.FullLoader))
with open("test1.yaml","w") as f:
    w={'a': [1, 2]}
    yaml.dump(w,f)