# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

Website: [https://www.defund.app](https://www.defund.app)


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

**live-peers** (24)
```
peers="e3d98694b276a2fa3bd52a77d00d379f0aacb58c@173.249.7.166:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,b5f48558fd70799ae123bd879ce12205478be379@135.125.180.36:20756,58437bc62307a512f391db5c1e24e3cff8b9f8d3@136.243.88.91:2070,fe1fe3318b450201b19827bbdf9d5aeb9ae2b916@207.180.236.115:31656,4c170418a04a65b74fb17880aaa25674aae1451f@23.111.154.14:26651,175cdc1cae6635d5779e8870a20f761f1d58f02f@65.109.51.41:36656,0b141f72551552a5faf109413292e72408a34c34@65.109.27.156:32656,4c291b33574d679e43f7cec340ba4befecec0724@161.97.152.115:26656,ad35b87df11c37b5f66931cd86c5dc2853aabae2@95.216.69.88:36656,dca3bab49d1d93eee0ae15aef78cca2809e657f1@170.64.138.160:26656,f8e7b1b8382b9d4b0c04274826a89682ad4b5bfb@62.171.143.40:26656,27184beff22d064a593233bbe6b0883f9f7fc2ff@45.87.104.74:26656,d1976601f04df2a2c7e35c0e8212464acfb7512e@75.119.147.235:26656,36909ce5289d8f994fb2562f7a188a79ce826359@141.95.145.41:27656,d9d5f9a4ca3cb5ab7db0e6735b0ce8c246eceb6b@135.181.214.190:26656,e199e4d17120559bc34357d72f6595cbcd4d5cd4@173.212.216.232:26656,4758cb09f15174708880c0986bb0b57af4dc5d5d@135.181.208.169:27656,e104f008f6d1227170d3b4ce1d73f0ea2068094f@84.201.162.168:26656,53e2240528947ff8f7b037d347b7258f05ce88f0@89.179.68.98:27656,e4470dac98f2cee5bd060c52c7d801d57bfc9308@185.245.182.206:26656,b712dfb6043ada3c0b981a4a5ec6b5f7658cc4d8@173.249.51.180:26656,c0637ffa6e3a9a92c88820a8320ee58fb807706f@142.132.253.112:40656,0a8430b93bd3ddbf247388ca638512981ff07eaf@195.3.220.9:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
