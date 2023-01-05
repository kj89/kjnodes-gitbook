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

**live-peers** (23)
```
peers="6c0024b454c7e001b98ab04692c9d616d403bb7d@176.9.146.72:40656,f5c51a2c40257da4524776717f91590ccad593ec@176.124.221.134:26656,67742399a48abc97c7eef61b1a60b96c720122c2@45.147.199.180:26656,d31d9801e7a021d287570b94ffcf27b91b0d9b66@217.76.55.74:26656,9dd945f369a7aa1946e007d9547b364e69da7db8@185.192.96.140:26656,85279852bd306c385402185e0125dffeed36bf22@38.146.3.230:11256,a78c5a1fa7b12eef729fa3dec3b7c3b073552664@45.147.199.191:26656,f0e1b5cbade7abe4a23fb12d0359c5bc40213718@95.217.109.222:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,4c291b33574d679e43f7cec340ba4befecec0724@161.97.152.115:26656,f329bee02e530e05a8937887c8ea4e75851281f1@194.180.176.126:26656,b914bb37cc8d1b7fb91579a79f7438a24d16de65@45.147.199.172:26656,34caa18dc803a7c1c5da380f85f18bbf6e2e6126@162.55.33.123:26656,95d487c4f51295c4cd799cc7fe53d23ea7298bdf@206.246.71.251:46656,d1976601f04df2a2c7e35c0e8212464acfb7512e@75.119.147.235:26656,cb503107b4135363d5ff83ff6a1a1423d8db4166@62.171.169.230:40656,d7c675fa2eef507d4e2270c442383a886cade959@207.180.248.230:26656,e199e4d17120559bc34357d72f6595cbcd4d5cd4@173.212.216.232:26656,98a777dad655ddfbca503742107ff63fc5e0a9f5@45.147.199.212:26656,6854d36513081c77a24987ab66a436e29e3e5cfa@65.21.131.215:26576,8ee475f4b4574176f4e9d5d111dba6724e0ad62b@37.120.163.114:26656,b9a22be1f13a4ed99de4ecdd4c9e2a9e4711c2ac@45.147.199.190:26656,331bd82dc918ffaaf75284ae54b35bbb94f8e216@144.126.138.249:30656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
