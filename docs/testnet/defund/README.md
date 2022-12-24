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
peers="e80137c82b7afc3f399bc2be3e2b4162957de04f@185.209.230.89:26656,0a8430b93bd3ddbf247388ca638512981ff07eaf@195.3.220.9:26656,d1976601f04df2a2c7e35c0e8212464acfb7512e@75.119.147.235:26656,8a650a9761db8abc1096abc3d4a68431600ae835@62.171.149.101:46656,78bc2e1ab3406de82c99345a0135c77543a5d018@194.146.13.223:26660,0b141f72551552a5faf109413292e72408a34c34@65.109.27.156:32656,95d487c4f51295c4cd799cc7fe53d23ea7298bdf@206.246.71.251:46656,06869237862f0d21266f2182f2dc4e4b319a0168@194.163.189.179:26656,4c291b33574d679e43f7cec340ba4befecec0724@161.97.152.115:26656,ad35b87df11c37b5f66931cd86c5dc2853aabae2@95.216.69.88:36656,a78c5a1fa7b12eef729fa3dec3b7c3b073552664@45.147.199.191:26656,c3643415250344482ed22520e06770cdddccf5f1@185.202.223.158:26656,175cdc1cae6635d5779e8870a20f761f1d58f02f@65.109.51.41:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
