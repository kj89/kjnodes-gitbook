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

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (35)
```bash
peers="45cc764ce4547208c21f62340a280cff1f2a4ab5@5.9.147.185:26156,ee812a11525cf7e2de4bd63e66aed8b8de337902@38.242.235.199:41656,6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,016b0e565abd496b9473b87ac41339251005d12e@194.163.167.163:41656,798cf016b5150592badc8257402312fc50b7361d@65.108.45.200:26878,b5fbf2633a1d00c4e0e62f1e0012f8e72af15aa9@185.218.124.169:26656,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,921348b18868c83bfc5375fc9860bb28aaaf0d0e@38.242.238.229:26656,b3a5eb9f148cfd8c36e28c3648e2f9cc4270dfd0@139.59.163.245:656,61d2b313e2adc9d7990944f8ab5a6f9ecf08084f@65.21.122.171:16656,e1ab0573d55ff92fad55d2929e353904f1bbe36f@135.181.16.252:31656,74a4bbfbf4d1ca9852d10f3a97e4d012c62aec9e@146.190.102.111:41656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,3e5ba61e8481c6c71d3f2cc022dd6671ed7cacf8@65.21.170.3:41656,5b1c25f4dff541f77f1532c457f73ca7ee2e4c18@194.163.170.225:26656,7109d229fe6c1f952e6683e4ce99d57aab38f7cf@83.229.85.125:26656,4210af79e9137b8647174c003b6b329caaa8e3da@95.217.85.254:15609,995177c4b8c2b498de50483a614f9e30bf02e843@65.109.130.180:26656,3b7845f8c8361c2f2de742473cd891c6e8cdeabf@83.171.249.159:656,5f4aee494e44d65f31753d7122f074f27b3ed8a2@95.216.162.25:656,292c099fc654a1331d3b62a1b939f867b62ef434@45.85.147.242:656,53b421af01f3260e949d6a9c2dc09e3b1dbf9fb6@109.205.181.30:41656,299787b65bc3f176cdfc126af491c282f8e33a85@164.92.107.81:26656,7182dfadba43a9a3b35f6862e63f75be20c8b1db@95.217.214.125:41656,0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,9a864058d9272928db234050a45ac8ad439aa967@164.92.109.65:26656,231ded997a112e8778afed3fd07ed7b98e0686e0@167.86.91.80:26656,e511a5b55979b7d630f016e2b15b513690fd3e33@185.239.209.124:656,f97115243c6291081b546e8d59f51e5ecede4168@149.102.155.225:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,0b1ba8849c79f41d027de35f98398d1da6a0126e@38.242.229.50:41656,c19da021d6bbdeccdd03453a021d7171e6e299d5@173.249.14.30:656,37c3d29df83da59e5a258d413e2f89365ab05711@85.239.243.12:656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,200b0594c8bfd86c1fc2a5b5c72e266139f3b193@62.171.140.239:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
