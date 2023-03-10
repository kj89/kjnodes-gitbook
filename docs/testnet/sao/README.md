# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/sao.png" width="150" alt=""><figcaption></figcaption></figure>

SAO Network is a secure and decentralized Web3 storage infrastructure  based on Cosmos SDK and IPFS protocol. It aims to facilitate the adoption  of Web3 storage, support the growing demand for Web3 applications and  allow for a more decentralized way of storing and accessing data.

**Chain ID**: sao-testnet0 | **Latest Version Tag**: v0.0.9 | **Wasm**: OFF

[Website](https://www.sao.network) | [Discord](https://discord.gg/f4xzfvPhhA) | [Twitter](https://twitter.com/SAONetwork)




## Chain explorer
[https://explorer.kjnodes.com/sao-testnet](https://explorer.kjnodes.com/sao-testnet)

## Public endpoints

* api: [https://sao-testnet.api.kjnodes.com](https://sao-testnet.api.kjnodes.com)
* rpc: [https://sao-testnet.rpc.kjnodes.com](https://sao-testnet.rpc.kjnodes.com)
* grpc: [https://sao-testnet.grpc.kjnodes.com](https://sao-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@sao-testnet.rpc.kjnodes.com:49656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@sao-testnet.rpc.kjnodes.com:49659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/sao-testnet/addrbook.json > $HOME/.sao/config/addrbook.json
```

**live-peers** (35)
```bash
peers="51064e987ab1193713957b6e07a70589d97d2903@157.245.197.58:26656,3c769db2e0332c1728b87173084cdc9dc1ab24b2@65.21.134.202:15756,04f9bad9b3b5c657dc7c11b341074028fb2faf2c@203.23.128.181:26656,2f5b05d5a8fe73c7dd2830c5face9c1b5316cdc8@65.21.131.215:15756,651a0314b0563c187691a4ff7e715b8dfb32eaa6@64.226.71.203:26656,0c77942550c78ae8939b691b725a9dd7ffa4d864@185.219.142.182:27656,a8dc98984aff5131b04afb408ac605fabfc5bfe4@64.226.72.32:26656,b417aa497b83a616ef77774773c3071fc216aad0@206.189.59.199:26656,8eddcbb5682d375de489518fe41620d04518d116@188.166.182.215:27656,e926078d739912b6c843503c13168dee2af6a207@45.14.194.30:26656,1d4c2290729dad5a5cb464b487e2922b88e0d4e0@65.109.117.23:49656,be4d5db39afa804eb2eb9c44acecb43efd4527dc@65.109.81.119:21656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:49656,923df3e7e591a5716d51809e9366483fd3926a38@5.188.118.105:36656,d53118a48bfd3be582f9ffb4b6fefb5af3d31cac@116.203.226.63:26656,c6d7c5c8d8b780756f9ff31ef735221c4a589220@31.220.72.135:26656,91b67dd0d2904d95748e1ec5311e39033cfeaabc@65.109.92.240:1076,4823f49a75b4cec46e4411a3acd9e4ef55547485@157.90.226.166:26656,8028ba794ab03b98518cf0e3a76256dd4c82ff11@138.201.248.108:49656,4f7898c70637f2a5c65ea909afcd47c10f090863@213.133.100.172:27544,6642a126fbf5b2f8aa2f22dc169a9bb98f1c17a3@170.64.188.152:26656,48e9d12ec0e2cc80770777f0896429fd4d44d39d@209.126.13.77:27656,f64f50dd41caf5f05ee1d567ead0a46feb4dec50@164.92.173.124:26656,bf34e92211b840f044f8aed66455a73f9c7a4e10@167.99.73.24:26656,2391c496886d549eaef56eec922193b23e48119f@65.108.12.181:26756,e72060f6ece326a600be7854624f1731227c2c6c@113.161.144.108:26656,0f73577b17dbf79f4d7d9d8486684357477cd400@143.198.136.136:26656,3369d58ada8a5457c35b6710f2bd5216b863993f@34.106.73.81:26656,14e4a9a565508d0aac31f270d898fb6df82f1146@42.117.129.1:49656,025e75f3da8d3c760fcc0c7b16919b2b6e58c783@165.232.156.214:26656,bcb3f05e4b63a0e8dc5c57870e0412169d3a2290@109.123.243.68:26656,ada0a0b4b5b3d290cae51b946b33a1079d00df72@185.197.250.35:27656,ac3e7d132b2fac1e13887d4af129ec1998bbebee@66.225.243.53:10656,392a04576cd1cd19dfe2f065bcd911acfadff5f3@217.76.59.212:49656,31a7e4c42a765821aea41f1b09bb50181c4415a1@65.108.149.17:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.sao/config/config.toml
```
