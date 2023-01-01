# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (14)
```
peers="d3b7991e387ebfe26965fe4361bc0f27789b0aa4@38.242.153.15:40656,67742399a48abc97c7eef61b1a60b96c720122c2@45.147.199.180:26656,ad35b87df11c37b5f66931cd86c5dc2853aabae2@95.216.69.88:36656,b9a22be1f13a4ed99de4ecdd4c9e2a9e4711c2ac@45.147.199.190:26656,c640df433e42f07b2d2ea11679c35a69174f6ef2@194.180.176.124:26656,c734239cb2a4a59e69de4fc52a9c4aca57285391@199.175.98.107:26656,0a1fcc2907e50b46f021389049c79f7d124f9946@77.51.200.79:36656,4c291b33574d679e43f7cec340ba4befecec0724@161.97.152.115:26656,e80137c82b7afc3f399bc2be3e2b4162957de04f@185.209.230.89:26656,5e6354412f3742ac76e37838236707b373c1de43@185.250.37.162:29656,98a777dad655ddfbca503742107ff63fc5e0a9f5@45.147.199.212:26656,2093ca0548db1553f55ad5a983ce154d04ed5ea4@146.19.24.52:40656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,8ee475f4b4574176f4e9d5d111dba6724e0ad62b@37.120.163.114:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
