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
peers="3989c44e8af3427b22a71a94185e85df99d450b4@149.102.158.188:41656,591318ade07c267271bb27790acec9e80dc1ce14@65.21.105.9:26656,995177c4b8c2b498de50483a614f9e30bf02e843@65.109.130.180:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,f314268ef1886e4ad2801c8443ea0b0c8143a246@95.214.55.25:30656,33196fb0090d2de3671e36545d3425f641c9c0dc@65.109.70.4:41656,5c74fe6868cda2003926c0a6299c9cebec5c4d1a@65.21.239.60:41656,7182dfadba43a9a3b35f6862e63f75be20c8b1db@95.217.214.125:41656,c78af3c8a2fa3d398dedb1ad9052eaf60dc27434@95.216.163.254:41656,16a287d1ecb484edb55244446efd38f360f7e5a1@65.109.90.61:41656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,c5fa8b2df54c71b7a6479d9ba67dcd87b7109f25@103.104.75.230:41656,dff75265c391b88c8a7593960b499613afae437b@146.190.92.134:41656,19fb417249992ae8def277fb753656da318fe250@38.242.133.239:41656,ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,8e9c65f65157cd5540e94335ae068c4040cf9b3b@83.171.249.165:656,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,38f4e436b28b05850fa9b67cadf0700123cec094@45.10.154.166:26656,5fb72a0bea398ce56fa20cd732623f98d774be7d@149.102.128.208:41656,0eb70bf5e2403694109f9bba184570074c2dfdd5@38.242.235.255:26656,539da540605f44f63264fb1d49591fe387a83c17@159.223.50.54:41656,61c85d47e1dd86d5a5849450b849078d4d13184b@85.239.244.123:26656,374da78901e59810277fc35482bce6e30953f488@80.79.6.155:41656,6ce7f9ea8e3019c50057f4eb2a0ed55e8eedf874@194.50.0.44:26656,aba9c58344ec5e7dcd5ea1dc273d853e58b2ddd9@37.187.78.201:41656,5f4aee494e44d65f31753d7122f074f27b3ed8a2@95.216.162.25:656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,c03e9f152bb1becc54d4424d02249135d39be09f@81.0.218.106:41656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,5f045d143cdf9ac78821e848cb10f9c861f5e272@89.117.56.126:24256,02c20307295465ab2592fd81176e66be90d4bbe2@5.189.159.111:26656,c19da021d6bbdeccdd03453a021d7171e6e299d5@173.249.14.30:656,ccf24b1e4f8566f3914c08e13d2b6154ed47ddbd@45.153.48.45:26656,72bac43328190fa83cbcb4e45abd9b96014122b8@164.92.255.96:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
