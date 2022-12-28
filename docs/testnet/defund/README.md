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

**live-peers** (26)
```
peers="c640df433e42f07b2d2ea11679c35a69174f6ef2@194.180.176.124:26656,de3c08f842d170d0cb3f8d1e074678466bf8fd7d@185.202.223.154:26656,c3643415250344482ed22520e06770cdddccf5f1@185.202.223.158:26656,d1976601f04df2a2c7e35c0e8212464acfb7512e@75.119.147.235:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,2093ca0548db1553f55ad5a983ce154d04ed5ea4@146.19.24.52:40656,95d487c4f51295c4cd799cc7fe53d23ea7298bdf@206.246.71.251:46656,0a1fcc2907e50b46f021389049c79f7d124f9946@77.51.200.79:36656,d368e8fc76143f89e53f0997fd5dfef32129168c@109.110.63.204:26656,e199e4d17120559bc34357d72f6595cbcd4d5cd4@173.212.216.232:26656,a713c7dbfbcf0704f591bcc07d1f116303c44b27@45.87.0.238:26656,d7c675fa2eef507d4e2270c442383a886cade959@207.180.248.230:26656,f329bee02e530e05a8937887c8ea4e75851281f1@194.180.176.126:26656,6854d36513081c77a24987ab66a436e29e3e5cfa@65.21.131.215:26576,9e3c8603f8eb1aeacf7392701a1977668684803c@194.163.170.245:26656,34caa18dc803a7c1c5da380f85f18bbf6e2e6126@162.55.33.123:26656,fe1fe3318b450201b19827bbdf9d5aeb9ae2b916@207.180.236.115:31656,fd2122d21e10253a86739bdd33686065008926ed@85.10.200.221:29656,175cdc1cae6635d5779e8870a20f761f1d58f02f@65.109.51.41:36656,fd3f439c775df4a7c1ced33d613124acee4187a6@194.163.154.129:40656,b9db73c9cac1676cd389711a18a4a64eb6ce3614@135.125.153.176:26656,b9a22be1f13a4ed99de4ecdd4c9e2a9e4711c2ac@45.147.199.190:26656,aee64a0d9b4f06f9f0949650fa22494b1cee1d58@84.46.244.228:26656,c734239cb2a4a59e69de4fc52a9c4aca57285391@199.175.98.107:26656,9dd945f369a7aa1946e007d9547b364e69da7db8@185.192.96.140:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
