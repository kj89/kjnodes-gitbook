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
peers="f9b892ea2e8ed8aa83f7b98e7e47371c23b01924@213.239.207.175:36656,3e5ba61e8481c6c71d3f2cc022dd6671ed7cacf8@65.21.170.3:41656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,bd7c6c83af99edf0ee5b857a99997fb9fc8f40a7@65.109.116.204:20556,a8e74ebf033def6fbb28d1b846d7a6c275ad2ef1@65.109.65.163:20556,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,59cdd2944de1d9eccdbb013123f2dc8b6a5770f8@178.18.254.33:26656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,37c3d29df83da59e5a258d413e2f89365ab05711@85.239.243.12:656,52ba59360cfc90c8beb1c3704a4c9ed9b38e597d@65.109.65.126:41656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,6e586e45f8a9d73333d24cd0fa7f64abc8be6d2b@65.108.226.183:11356,dbea2239b43c9e45913c22ad091abb8aaf7db469@190.2.146.152:33656,5c45e8920c5094827ec5afaca9ab469aaa0b4eaf@65.109.88.254:28656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,9cd6d2477d278ef6ccffa5cc4e22fd0d9489cd23@85.10.199.157:34656,820024c34989e7605d9367847e1fc2d01ad763bd@65.109.92.235:30656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,5b1c25f4dff541f77f1532c457f73ca7ee2e4c18@194.163.170.225:26656,6da2faa11e21db872cc64a975160a55b5fc9166d@149.102.128.203:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
