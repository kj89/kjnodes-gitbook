# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/gitopia-testnet](https://explorer.kjnodes.com/gitopia-testnet)

## Public endpoints

* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)
* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* grpc: gitopia-testnet.grpc.kjnodes.com:41090

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

**live-peers** (30)
```bash
peers="1983d3cbcbc281232b5946ba9a2487e8f6976817@149.102.148.141:26656,d2975b49708dc92ee3b7da1d72e3eee3119d1d0c@167.86.105.216:656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,52a2fb0aa22551b1ef0155824228924d41c1daa6@85.239.230.213:26656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,bc688b2be879ba5bfa34587e096a9c9a4df2e6d4@45.151.122.116:656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,5f4aee494e44d65f31753d7122f074f27b3ed8a2@95.216.162.25:656,37c3d29df83da59e5a258d413e2f89365ab05711@85.239.243.12:656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,81f9bdd0e1e01390b70df7544b45efdccb52e41c@84.54.23.199:26656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,01daf430f5c4b6aebe4aa94ee3724f3deec2279f@85.190.246.173:26656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,cf97c77d4f28c3bd619efe10f4f9aa404f246853@161.97.154.51:26656,ba614c2b5beae6df39a4310043294ffde60e8e8d@45.85.250.147:26656,63c980b1d82318e2e75c15e5b950d8a38a42e1b1@38.242.142.170:26656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,68829bc3c3204eb67c1f913de89f05b12f2b8e19@79.120.77.57:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
