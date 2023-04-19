# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: orbit-alpha-1 | **Latest Version Tag**: v0.2.6 | **Wasm**: ON

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/defund-testnet](https://explorer.kjnodes.com/defund-testnet)

## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: defund-testnet.grpc.kjnodes.com:40090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (30)
```bash
peers="a79130668102f116a23cfcf9fd94623de4a223fe@81.30.157.35:10656,11c0952beaf78a6452d270c7bd344c25406e1b16@95.217.212.66:26656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,0634225db2052d7b42f64d63d3d3f9edbbbb9309@65.109.104.111:56108,2788c4e5178166010baf8786ad3091a9fcc1a730@5.78.101.216:26656,33527195a479780ce40322433f1eca5d11bc47f5@89.163.140.70:26656,288bafc7978c4e9adee447a06b97de11c87c7227@185.202.238.250:26656,1b16614a7f8c703db882dc44095c12c9e4d21900@89.163.240.178:40656,bba79e883e47c07cfee15e1eae803bd063a56ea8@65.108.41.83:26656,14d989a7ff26fd1aba1349497bb9ab0f8ed5c078@109.123.254.14:26656,9446504166663fc0090b81abdf86fafe93e72a40@185.209.30.95:40656,c1c6cf5859c43fb3acd19ccdb78a4caa0a151ff7@45.85.249.107:27656,aa3878e41e692cd7530387d94fd02012dd025b40@135.181.93.86:40656,fb124c136c3aa20a71c68d9cb0a2833293c8dc58@23.88.73.158:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,22fa766ffe457fd1236ea88bce1f40bf4bbaf328@77.91.100.131:26656,d3f613337f8b4c52fc7363e70df93422327ea925@23.88.32.193:26656,fe95d64b71c3bccfb60db55dff0c5bd229306b1d@107.155.98.222:26656,b1b373b8b692ec5a134ad583c0522af279ee2b6e@176.9.151.221:27565,185d68d4207c006f980001c04bc5c5b9bc097874@88.198.48.50:26656,bda598af0c96d72a85c3b6840138d929b8c4e762@84.46.248.207:26656,afdbe2fb845ff591d32f83e4a28b49c59cd9111c@65.109.117.121:13656,6999cca6c55576a48d4f227b87dc904fbdb085aa@65.21.134.202:26576,8abfa09fdbea667157d96f79c815fd9b3186b6ae@65.109.92.240:2026,c66d4d22039ad8afc8cc3cc873c69e2ddc37e70f@185.155.97.74:28656,23c52b4aa95a5b269277292410f6f4c8815e616c@194.163.174.103:27656,0eb9422efedd714d3db57d1ddfaad75f80a60518@5.161.99.35:26656,acad4439671fef4e64e904587a81ee9c34e9505d@95.216.214.103:40656,6047d282f126e8be4b36ca28c0cc3d244577f798@159.69.185.109:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
