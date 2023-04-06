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
peers="4e4f87cfa1993f4f3f7645c41f469987cafdf960@85.10.202.135:12656,37677351ed74a5ced46a99217d19e30d5bcacc1d@5.75.147.138:26656,eaa9978430e55663346eb61312cd5ecc21448b25@38.242.139.153:656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,6e586e45f8a9d73333d24cd0fa7f64abc8be6d2b@65.108.226.183:11356,292c099fc654a1331d3b62a1b939f867b62ef434@45.85.147.242:656,f13a4cb3ca18c1de6232e901c8feb209f0945954@65.109.65.248:26656,007d2419fea80aee707d009af0153f5105c53379@38.242.139.164:656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,f7fcda07044dc64cec2f6dca9da0c37a254bbae8@138.201.127.91:26676,4cd60a4dd4211d38d948a86a614f1fd8d3d274eb@75.119.153.139:656,1f7f58f130ea9c89be44fd60554d5e97da56c395@206.221.181.234:56656,cf97c77d4f28c3bd619efe10f4f9aa404f246853@161.97.154.51:26656,0150c41282284a9546f8fe0f2531fc6b9d9128a3@65.109.23.114:11356,968d1b36aca27cae9ea0c335989bc0f8f6b5096b@62.141.46.165:656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,f2bca9113807369ff96cfed3639bc6d65467e76d@149.102.159.81:26656,27411a4ba3fae9b1bb00b1181da0ea300947418a@65.21.254.21:26656,c78af3c8a2fa3d398dedb1ad9052eaf60dc27434@95.216.163.254:41656,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,f0a82f850a0da74c32836b125a52bdfd9a78fdd7@65.108.105.48:11356,d9d6cba678f8630d9ab507254dc19949083afb7f@13.49.137.73:26656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,9910168225ef5b2075890b8aa8d58cdd428f6429@38.242.145.87:26656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
