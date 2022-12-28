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
peers="66116d559390844588c67db54b894779cf00d559@5.9.61.237:41656,4ed110a5b1ebad62d1e92e8cdabfc9160e2ca4db@65.109.92.148:46656,af44ee207881ea315ded748adf2c461cde5fa792@143.198.138.43:41656,0eb70bf5e2403694109f9bba184570074c2dfdd5@38.242.235.255:26656,407eb21b784f1dc4e9902cb812b65eec760c6a19@185.193.66.67:656,67e839cff368a20c9b7a1390b739d3538866b0b6@65.21.134.202:26356,ad33cf22f96e43448798686ed0f7428b8fdacf5b@5.161.90.174:656,f1c042fca05e4bfb9a6da1cccaa5108a26ea1e0f@65.108.104.167:28656,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,5f045d143cdf9ac78821e848cb10f9c861f5e272@89.117.56.126:24256,c03e9f152bb1becc54d4424d02249135d39be09f@81.0.218.106:41656,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,f97115243c6291081b546e8d59f51e5ecede4168@149.102.155.225:26656,016b0e565abd496b9473b87ac41339251005d12e@194.163.167.163:41656,ff4fab3a07cdf3601b90ececd2de9a85b3a1a42e@82.208.21.152:26656,73de34b1d08fdd58b5a5c0ec6d2560310c1ebe90@38.242.151.86:26656,e9d73e8a301d4d55298b2b0aa35d59348a10012b@164.92.95.212:26656,8e9c65f65157cd5540e94335ae068c4040cf9b3b@83.171.249.165:656,ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,3bcba60fe08bb6ce59abc19b84cf58e7c915e0ed@193.46.243.243:656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,c5fa8b2df54c71b7a6479d9ba67dcd87b7109f25@103.104.75.230:41656,72bac43328190fa83cbcb4e45abd9b96014122b8@164.92.255.96:26656,47f18762432fc57e8a50569a6326ce06b60a971a@154.26.139.97:41656,d0ca7d1e144eee74396b1c7a98737e4ca2ced2bb@137.184.30.252:656,3989c44e8af3427b22a71a94185e85df99d450b4@149.102.158.188:41656,e511a5b55979b7d630f016e2b15b513690fd3e33@185.239.209.124:656,dea00215e54c4098a4f194a7ecd43e24ea99336f@88.99.95.81:26656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,5c2c2b27e1824097d4f5dc7a581a8d615923e76f@185.252.235.110:41656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,38f4e436b28b05850fa9b67cadf0700123cec094@45.10.154.166:26656,292c099fc654a1331d3b62a1b939f867b62ef434@45.85.147.242:656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
