# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (35)
```
peers="b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,4ceba74efb843cf10926a9ec757e4e2081d71e92@207.244.226.183:656,0eb70bf5e2403694109f9bba184570074c2dfdd5@38.242.235.255:26656,165c6969e40fa2ae2340d8e9fa79a14589a46406@185.193.66.202:26656,3989c44e8af3427b22a71a94185e85df99d450b4@149.102.158.188:41656,eb34bba81406640084995e7a3f732187509ae2e8@164.92.113.87:41656,d9b86c9459ac8bb4760d37095732ccd2746aca1f@65.21.131.215:26356,ccf24b1e4f8566f3914c08e13d2b6154ed47ddbd@45.153.48.45:26656,5171aad5f862d474b36fc8049be3339068c96cc9@165.232.151.144:26656,c5135fa9a85fed11a54395df5d5df3c4262d99f1@185.245.183.241:26656,09538ba6159f454a17d76501c59e23bad6fc9d3d@85.190.246.67:26656,615b82e2721e06770a71ac3a0328d0e4f0eea0de@81.0.246.222:656,63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,d0ca7d1e144eee74396b1c7a98737e4ca2ced2bb@137.184.30.252:656,6871aeacd353d66c38b1ebbf3b1ad244fa05e32b@167.86.84.125:26656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,5c2c2b27e1824097d4f5dc7a581a8d615923e76f@185.252.235.110:41656,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,8e9c65f65157cd5540e94335ae068c4040cf9b3b@83.171.249.165:656,61c85d47e1dd86d5a5849450b849078d4d13184b@85.239.244.123:26656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,ebeba690d8084592a983da1e6429598cc9b9d04c@213.202.212.77:26656,a6f4fd8efe8a575a15e25652ecebce3fa1ed62a0@213.239.217.52:35656,31099d763305ead833b84c28b142ecbfd3628a64@85.190.246.250:41656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,798cf016b5150592badc8257402312fc50b7361d@65.108.45.200:26878,fea7c372588898f7ea3a04373c52a30712b3c279@185.239.209.56:656,2ef464f5acb300ed319f18fb082c7455a05e7cca@89.163.209.88:26656,02c20307295465ab2592fd81176e66be90d4bbe2@5.189.159.111:26656,72bac43328190fa83cbcb4e45abd9b96014122b8@164.92.255.96:26656,5f045d143cdf9ac78821e848cb10f9c861f5e272@89.117.56.126:24256"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
