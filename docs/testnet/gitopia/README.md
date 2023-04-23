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
peers="d2975b49708dc92ee3b7da1d72e3eee3119d1d0c@167.86.105.216:656,0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,45c07c07c311ae9dec3e4090f7ad94a9f5aa09c4@94.131.119.90:27656,8d45cada398e1035e220857a84021fabfa723248@2.58.82.21:26656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,1983d3cbcbc281232b5946ba9a2487e8f6976817@149.102.148.141:26656,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,12430b7b784cd2ffb3e3265836167adfe06aeca0@146.190.48.205:26656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,52098a0fdd0dc566615ad37492019d252635bdda@45.85.249.131:656,ef8bf45c54182573c9a852e8181f43838e198467@185.245.183.253:41656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,93c4c73375b5f52020e7e7bd3f901ee28f07e6b7@109.123.243.66:41656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,37c3d29df83da59e5a258d413e2f89365ab05711@85.239.243.12:656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,be9868fe956a89edead0720d8c2ff31e6093d4c2@94.130.218.86:10656,ac606e28c081c679dc23d9a94c29842be8f8b1f1@45.85.249.133:656,0150c41282284a9546f8fe0f2531fc6b9d9128a3@65.109.23.114:11356,4ed110a5b1ebad62d1e92e8cdabfc9160e2ca4db@65.109.92.148:46656,f1c042fca05e4bfb9a6da1cccaa5108a26ea1e0f@65.108.104.167:28656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
