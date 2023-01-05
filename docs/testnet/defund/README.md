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

**live-peers** (21)
```
peers="5e6354412f3742ac76e37838236707b373c1de43@185.250.37.162:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,f5c51a2c40257da4524776717f91590ccad593ec@176.124.221.134:26656,3c838e2b140d36e08c406884ab75119c016c7938@159.69.217.0:18656,d7c675fa2eef507d4e2270c442383a886cade959@207.180.248.230:26656,7ca31e50d5509104ea481869bcbe91e6883fe9d0@135.181.150.198:36656,ba0d5a6bc703e375067befcb601bf529805cec64@144.126.143.183:30656,c3643415250344482ed22520e06770cdddccf5f1@185.202.223.158:26656,c734239cb2a4a59e69de4fc52a9c4aca57285391@199.175.98.107:26656,219c417bd9de04c60f730abd4769e981f10c083b@109.123.249.191:26656,f4869f02f970f222d81718a7a2fcf9b3c7b1b10c@109.123.249.189:26656,98a777dad655ddfbca503742107ff63fc5e0a9f5@45.147.199.212:26656,58d46050cf77065d27e9526a7e93c8f814cc036a@194.146.13.185:26656,4d3b782ab389525370f53d40e970b1362bc92106@185.182.186.202:26656,0b141f72551552a5faf109413292e72408a34c34@65.109.27.156:32656,d3b7991e387ebfe26965fe4361bc0f27789b0aa4@38.242.153.15:40656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,d368e8fc76143f89e53f0997fd5dfef32129168c@109.110.63.204:26656,b9a22be1f13a4ed99de4ecdd4c9e2a9e4711c2ac@45.147.199.190:26656,b914bb37cc8d1b7fb91579a79f7438a24d16de65@45.147.199.172:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
