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

**live-peers** (12)
```
peers="d3b7991e387ebfe26965fe4361bc0f27789b0aa4@38.242.153.15:40656,e22fa947cb931de73fa6b4ce58d3759dbd1c0129@164.68.103.176:26656,58d46050cf77065d27e9526a7e93c8f814cc036a@194.146.13.185:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,edabbcbfb21c488be785f0925b0060c717440bad@92.119.112.229:26656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,c734239cb2a4a59e69de4fc52a9c4aca57285391@199.175.98.107:26656,0a8430b93bd3ddbf247388ca638512981ff07eaf@195.3.220.9:26656,4d3b782ab389525370f53d40e970b1362bc92106@185.182.186.202:26656,f5c51a2c40257da4524776717f91590ccad593ec@176.124.221.134:26656,d7c675fa2eef507d4e2270c442383a886cade959@207.180.248.230:26656,98a777dad655ddfbca503742107ff63fc5e0a9f5@45.147.199.212:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
