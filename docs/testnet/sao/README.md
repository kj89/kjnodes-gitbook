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
peers="2f5b05d5a8fe73c7dd2830c5face9c1b5316cdc8@65.21.131.215:15756,651a0314b0563c187691a4ff7e715b8dfb32eaa6@64.226.71.203:26656,f4ebd48ae8b347eb71c43596f8c3b406807170ae@159.223.40.81:24556,3c769db2e0332c1728b87173084cdc9dc1ab24b2@65.21.134.202:15756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:49656,3535b3f6181b8ba413cd9391515b9840aafc4b2a@142.132.194.157:26256,1d4c2290729dad5a5cb464b487e2922b88e0d4e0@65.109.117.23:49656,449ad6d55f33ed9e70a93e7d9c630e43c3227f18@159.223.34.78:27656,51064e987ab1193713957b6e07a70589d97d2903@157.245.197.58:26656,a8dc98984aff5131b04afb408ac605fabfc5bfe4@64.226.72.32:26656,536ed23e7e75b3173da835995eec36be4b25dbc3@194.233.73.34:49656,9248e2c9d075f095ea2ada4cd86294f946d8678e@149.102.129.76:26656,902240030667c196d2857dd43da27f0fa83b5225@170.64.172.224:26656,b417aa497b83a616ef77774773c3071fc216aad0@206.189.59.199:26656,91b67dd0d2904d95748e1ec5311e39033cfeaabc@65.109.92.240:1076,61e9e3927c1d25d91e8fefbdc880791e7974bfb5@159.223.19.154:27656,006e207a3f235a28bc0815001b76ee385ee4bda3@88.99.164.158:1076,0c77942550c78ae8939b691b725a9dd7ffa4d864@185.219.142.182:27656,47971c889b727897dfc753ca93a15d8e1ce9cd5a@3.140.188.3:26656,e926078d739912b6c843503c13168dee2af6a207@45.14.194.30:26656,04f9bad9b3b5c657dc7c11b341074028fb2faf2c@203.23.128.181:26656,89a64a387e5ac190a29badcfbbedead3c0ab4069@89.117.50.5:26656,c6d7c5c8d8b780756f9ff31ef735221c4a589220@31.220.72.135:26656,5524049dff1e180a85adc2c9494f59c336e631fa@164.92.91.248:20656,bf34e92211b840f044f8aed66455a73f9c7a4e10@167.99.73.24:26656,6642a126fbf5b2f8aa2f22dc169a9bb98f1c17a3@170.64.188.152:26656,b697beb5417b0fb7ce8573986519c914f5ca6c4d@217.160.201.92:35656,627d0c6e30676a0b4bdb73a324b1eb3a08e5cc45@137.184.197.65:26656,ec7e0b075202f836feac71f017a90e0d83674cb8@65.108.9.164:24556,3369d58ada8a5457c35b6710f2bd5216b863993f@34.106.73.81:26656,1f8132e69cdc8f6b0ac73f32d18bba1472895c87@65.109.61.100:49656,9be082254c4f37aa089ae04a2ee78e5a856d6633@170.64.190.91:26656,5cea6b9e5a2ffd5f42a42515fefdd44a7631d048@101.80.228.209:26656,923df3e7e591a5716d51809e9366483fd3926a38@5.188.118.105:36656,e711b6631c3e5bb2f6c389cbc5d422912b05316b@213.239.216.252:41256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.sao/config/config.toml
```
