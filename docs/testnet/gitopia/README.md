# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gitopia.png" alt=""><figcaption></figcaption></figure>

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
peers="6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,f06f794dcc5964197da0e13709d71ea5e0f5b7f1@88.99.3.158:11156,975a3ade04fc92d00c7ad59d536506fde46169e7@167.86.96.233:656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,93c4c73375b5f52020e7e7bd3f901ee28f07e6b7@109.123.243.66:41656,0150c41282284a9546f8fe0f2531fc6b9d9128a3@65.109.23.114:11356,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,e17763e03ef6819b6f549b97abe9da7a1a7eeac8@164.68.121.241:656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,d318a60a25b7a84322a8083709ff8e8bbe82ddb7@65.108.13.154:26656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,6e586e45f8a9d73333d24cd0fa7f64abc8be6d2b@65.108.226.183:11356,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,38b327ce97c670014d52701e3a26eaa16fee1f7f@149.102.151.204:26656,7a755a2d4d5d609fed651662ebe37997256cff46@193.34.217.183:26656,ac606e28c081c679dc23d9a94c29842be8f8b1f1@45.85.249.133:656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,8d45cada398e1035e220857a84021fabfa723248@2.58.82.21:26656,8e20add7ed774bfd8600c628bb8fce87bacb207b@194.163.143.98:26656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,95c263a8bc8ef6dadbbeeeb242de4f89cf3c9657@193.34.217.154:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
