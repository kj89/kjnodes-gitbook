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
peers="d2975b49708dc92ee3b7da1d72e3eee3119d1d0c@167.86.105.216:656,619a23818cddd40d0b9f57e9754b719da13609bc@65.108.108.52:24656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,3e5ba61e8481c6c71d3f2cc022dd6671ed7cacf8@65.21.170.3:41656,0e9f303834a5d1f3be0babd5466725b3609ebc82@65.21.141.246:28656,cf97c77d4f28c3bd619efe10f4f9aa404f246853@161.97.154.51:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,1989ced6b71ce676a5ab4d0586d85e38fd41fbd2@136.243.88.91:7070,f9b892ea2e8ed8aa83f7b98e7e47371c23b01924@213.239.207.175:36656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,d9f6d67b593bb764656dbc686faed041928caa91@144.91.121.174:27656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,36363129015d1205f3c68f5a885af9528a12f642@66.175.234.44:41656,01daf430f5c4b6aebe4aa94ee3724f3deec2279f@85.190.246.173:26656,89d6b496813ea8f268b8410b34ddb2c86a726b6f@193.34.217.151:26656,f1c042fca05e4bfb9a6da1cccaa5108a26ea1e0f@65.108.104.167:28656,8d45cada398e1035e220857a84021fabfa723248@2.58.82.21:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
