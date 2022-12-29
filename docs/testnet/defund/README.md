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
peers="6c0024b454c7e001b98ab04692c9d616d403bb7d@176.9.146.72:40656,4135c03053c6f02e4ca773bee42d5c7f62922566@185.217.125.238:26656,8190bf19ef96627e3b35f2039ab6aeed551fa05c@167.235.201.57:26656,b5f48558fd70799ae123bd879ce12205478be379@135.125.180.36:20756,4eb0bef7997b87086c40766193d812479238187c@217.76.55.66:26656,28f14b89d10992cff60cbe98d4cd1cf84b1d2c60@88.99.214.188:26656,2b76e96658f5e5a5130bc96d63f016073579b72d@51.91.215.40:45656,f8e7b1b8382b9d4b0c04274826a89682ad4b5bfb@62.171.143.40:26656,d04084623a4ec44fd91d46f07ba2e2d1d0638dd4@141.95.23.183:26656,0e5c41bec481ae4da0577377bc1952eb29b1e4c1@65.21.78.86:26656,d9d5f9a4ca3cb5ab7db0e6735b0ce8c246eceb6b@135.181.214.190:26656,571d81a83ec9b23f953120b51440cf160d1c04e9@176.124.223.78:26656,35b9a1c3c7a597413f4c999a9fc1e6cb0cc8b978@65.108.100.53:36656,27184beff22d064a593233bbe6b0883f9f7fc2ff@45.87.104.74:26656,e104f008f6d1227170d3b4ce1d73f0ea2068094f@84.201.162.168:26656,0544670a43be0a61c7e354bc55d32b6573dc31cf@94.131.106.79:26656,f5c51a2c40257da4524776717f91590ccad593ec@176.124.221.134:26656,f4869f02f970f222d81718a7a2fcf9b3c7b1b10c@109.123.249.189:26656,b914bb37cc8d1b7fb91579a79f7438a24d16de65@45.147.199.172:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,9dd945f369a7aa1946e007d9547b364e69da7db8@185.192.96.140:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
