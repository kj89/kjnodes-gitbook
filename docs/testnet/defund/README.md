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

**live-peers** (24)
```
peers="95d487c4f51295c4cd799cc7fe53d23ea7298bdf@206.246.71.251:46656,c734239cb2a4a59e69de4fc52a9c4aca57285391@199.175.98.107:26656,4c291b33574d679e43f7cec340ba4befecec0724@161.97.152.115:26656,98a777dad655ddfbca503742107ff63fc5e0a9f5@45.147.199.212:26656,4c170418a04a65b74fb17880aaa25674aae1451f@23.111.154.14:26651,85279852bd306c385402185e0125dffeed36bf22@38.146.3.230:11256,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,9e3c8603f8eb1aeacf7392701a1977668684803c@194.163.170.245:26656,b914bb37cc8d1b7fb91579a79f7438a24d16de65@45.147.199.172:26656,d368e8fc76143f89e53f0997fd5dfef32129168c@109.110.63.204:26656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,a713c7dbfbcf0704f591bcc07d1f116303c44b27@45.87.0.238:26656,5e6354412f3742ac76e37838236707b373c1de43@185.250.37.162:29656,331bd82dc918ffaaf75284ae54b35bbb94f8e216@144.126.138.249:30656,57eadf177e7429db82bfdbed6fa0521e8741e404@94.130.13.40:26656,8ee475f4b4574176f4e9d5d111dba6724e0ad62b@37.120.163.114:26656,fd2122d21e10253a86739bdd33686065008926ed@85.10.200.221:29656,ad35b87df11c37b5f66931cd86c5dc2853aabae2@95.216.69.88:36656,175cdc1cae6635d5779e8870a20f761f1d58f02f@65.109.51.41:36656,edabbcbfb21c488be785f0925b0060c717440bad@92.119.112.229:26656,c640df433e42f07b2d2ea11679c35a69174f6ef2@194.180.176.124:26656,d3b7991e387ebfe26965fe4361bc0f27789b0aa4@38.242.153.15:40656,aee64a0d9b4f06f9f0949650fa22494b1cee1d58@84.46.244.228:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
