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

**live-peers** (27)
```
peers="0b141f72551552a5faf109413292e72408a34c34@65.109.27.156:32656,f329bee02e530e05a8937887c8ea4e75851281f1@194.180.176.126:26656,de3c08f842d170d0cb3f8d1e074678466bf8fd7d@185.202.223.154:26656,f4869f02f970f222d81718a7a2fcf9b3c7b1b10c@109.123.249.189:26656,c734239cb2a4a59e69de4fc52a9c4aca57285391@199.175.98.107:26656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,c3643415250344482ed22520e06770cdddccf5f1@185.202.223.158:26656,34caa18dc803a7c1c5da380f85f18bbf6e2e6126@162.55.33.123:26656,9dd945f369a7aa1946e007d9547b364e69da7db8@185.192.96.140:26656,b9a22be1f13a4ed99de4ecdd4c9e2a9e4711c2ac@45.147.199.190:26656,e199e4d17120559bc34357d72f6595cbcd4d5cd4@173.212.216.232:26656,0a8430b93bd3ddbf247388ca638512981ff07eaf@195.3.220.9:26656,edabbcbfb21c488be785f0925b0060c717440bad@92.119.112.229:26656,9c55522cc229ca89724d432f394374f1aa5269db@5.161.59.190:26656,d368e8fc76143f89e53f0997fd5dfef32129168c@109.110.63.204:26656,cb503107b4135363d5ff83ff6a1a1423d8db4166@62.171.169.230:40656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,a713c7dbfbcf0704f591bcc07d1f116303c44b27@45.87.0.238:26656,0d190196414307625a087a2d3cd02756fb4643a7@65.108.13.185:26767,9e3c8603f8eb1aeacf7392701a1977668684803c@194.163.170.245:26656,ad35b87df11c37b5f66931cd86c5dc2853aabae2@95.216.69.88:36656,98a777dad655ddfbca503742107ff63fc5e0a9f5@45.147.199.212:26656,b2521331cc7ef94374208aae2c1ed8a3dcdd811b@95.217.118.100:28656,4758cb09f15174708880c0986bb0b57af4dc5d5d@135.181.208.169:27656,57eadf177e7429db82bfdbed6fa0521e8741e404@94.130.13.40:26656,a78c5a1fa7b12eef729fa3dec3b7c3b073552664@45.147.199.191:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
