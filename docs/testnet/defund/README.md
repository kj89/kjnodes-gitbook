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

**live-peers** (22)
```
peers="b914bb37cc8d1b7fb91579a79f7438a24d16de65@45.147.199.172:26656,67742399a48abc97c7eef61b1a60b96c720122c2@45.147.199.180:26656,c0637ffa6e3a9a92c88820a8320ee58fb807706f@142.132.253.112:40656,4c291b33574d679e43f7cec340ba4befecec0724@161.97.152.115:26656,98a777dad655ddfbca503742107ff63fc5e0a9f5@45.147.199.212:26656,8a650a9761db8abc1096abc3d4a68431600ae835@62.171.149.101:46656,9c55522cc229ca89724d432f394374f1aa5269db@5.161.59.190:26656,57eadf177e7429db82bfdbed6fa0521e8741e404@94.130.13.40:26656,d368e8fc76143f89e53f0997fd5dfef32129168c@109.110.63.204:26656,a78c5a1fa7b12eef729fa3dec3b7c3b073552664@45.147.199.191:26656,d1976601f04df2a2c7e35c0e8212464acfb7512e@75.119.147.235:26656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,2093ca0548db1553f55ad5a983ce154d04ed5ea4@146.19.24.52:40656,00ddc480c7373130e1086c54173ce2bc5e0e2d45@185.190.140.81:40656,edabbcbfb21c488be785f0925b0060c717440bad@92.119.112.229:26656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,b9a22be1f13a4ed99de4ecdd4c9e2a9e4711c2ac@45.147.199.190:26656,a713c7dbfbcf0704f591bcc07d1f116303c44b27@45.87.0.238:26656,175cdc1cae6635d5779e8870a20f761f1d58f02f@65.109.51.41:36656,5e6354412f3742ac76e37838236707b373c1de43@185.250.37.162:29656,6854d36513081c77a24987ab66a436e29e3e5cfa@65.21.131.215:26576,c3643415250344482ed22520e06770cdddccf5f1@185.202.223.158:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
