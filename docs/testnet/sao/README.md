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

**live-peers** (33)
```bash
peers="51064e987ab1193713957b6e07a70589d97d2903@157.245.197.58:26656,e926078d739912b6c843503c13168dee2af6a207@45.14.194.30:26656,536ed23e7e75b3173da835995eec36be4b25dbc3@194.233.73.34:49656,651a0314b0563c187691a4ff7e715b8dfb32eaa6@64.226.71.203:26656,3c769db2e0332c1728b87173084cdc9dc1ab24b2@65.21.134.202:15756,6db6c1e8899bdc68e8637a75d984c03a7ff3d664@161.35.198.190:26656,2f5b05d5a8fe73c7dd2830c5face9c1b5316cdc8@65.21.131.215:15756,1d4c2290729dad5a5cb464b487e2922b88e0d4e0@65.109.117.23:49656,a8dc98984aff5131b04afb408ac605fabfc5bfe4@64.226.72.32:26656,91b67dd0d2904d95748e1ec5311e39033cfeaabc@65.109.92.240:1076,0c77942550c78ae8939b691b725a9dd7ffa4d864@185.219.142.182:27656,f4ebd48ae8b347eb71c43596f8c3b406807170ae@159.223.40.81:24556,5ed578e78207183e46bb009e2ae79745981f46d8@165.22.52.163:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:49656,bcb3f05e4b63a0e8dc5c57870e0412169d3a2290@109.123.243.68:26656,1b6164aab8350eeb71bd46ebfe641e5d103a3f8e@143.244.132.66:26656,7b6a37fcfbb8d614a78b91302b56d1f0ead2da13@75.119.138.113:49656,449ad6d55f33ed9e70a93e7d9c630e43c3227f18@159.223.34.78:27656,3da97cfdc72da7f3fcf4c62171fcbed421397785@130.185.119.243:49656,8c6201e793348d8f89dedcae6df3cd36198477fd@94.46.187.220:26656,0a661ed79b169c7c2b0f289c436e35900bb0de90@157.97.108.38:24556,8028ba794ab03b98518cf0e3a76256dd4c82ff11@138.201.248.108:49656,9248e2c9d075f095ea2ada4cd86294f946d8678e@149.102.129.76:26656,4245cbb64c958bb29a73048e37f8ccc68314b931@115.73.213.74:26656,8631d6d74cf6ad0906ab3602606ad64ae920a9a9@174.138.22.160:26656,9943703d74b9ce0fa43e45dd3a96f40141131b48@213.239.216.252:49656,3369d58ada8a5457c35b6710f2bd5216b863993f@34.106.73.81:26656,9fbe22df83c81bbe26e87cced299d29f418e03a5@157.90.226.166:26656,d1a6bf36766faf6265623f78ecaeafa87911b9c4@116.203.226.63:26656,c6d7c5c8d8b780756f9ff31ef735221c4a589220@31.220.72.135:26656,8776e3ef93a9bbb2b5a0bc6bc325c5fcf6f6e88c@35.204.153.250:26656,627d0c6e30676a0b4bdb73a324b1eb3a08e5cc45@137.184.197.65:26656,006e207a3f235a28bc0815001b76ee385ee4bda3@88.99.164.158:1076"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.sao/config/config.toml
```
