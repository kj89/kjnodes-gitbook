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
peers="f06f794dcc5964197da0e13709d71ea5e0f5b7f1@88.99.3.158:11156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,975a3ade04fc92d00c7ad59d536506fde46169e7@167.86.96.233:656,6b09dc9b3722ffa4d4da52ae3efee0af8afa72a0@65.109.90.171:26656,0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,5b1075a6a1073168e2b44b4ceceb02218ba7bab1@185.211.6.207:26656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,247dbc8048be7c024c5f5deee45c18bd2f19bc93@116.203.35.46:36656,9645f93ac2b57431a8ca32ac56b0ff63fe9c10ed@144.76.164.139:10656,f13a4cb3ca18c1de6232e901c8feb209f0945954@65.109.65.248:26656,9912d5c8d59b7736b0702b18aeb386efe7e46f3f@164.68.111.239:656,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,ac606e28c081c679dc23d9a94c29842be8f8b1f1@45.85.249.133:656,46dbff2358dddd99acc26c2d2ee5f204ccc347c7@217.76.61.242:26656,9b4bbef4aa6d11efc9ab8897e20bb2e56d1d7d06@157.90.208.222:60756,03073657e8bc5bcf71e7fd8df281ab8dcbc8821a@45.151.122.130:656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,314ee8896c9f9e39450dc25623f8019cf316ed60@38.242.135.124:26656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
