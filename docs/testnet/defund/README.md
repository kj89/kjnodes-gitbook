# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-4 | **Latest Version Tag**: v0.2.2 | **Wasm**: OFF

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)


## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: https://defund-testnet.grpc.kjnodes.com:443

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (11)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,a9c52398d4ea4b3303923e2933990f688c593bd8@157.90.208.222:36656,f8093378e2e5e8fc313f9285e96e70a11e4b58d5@141.94.73.39:45656,51c8bb36bfd184bdd5a8ee67431a0298218de946@57.128.80.37:26656,e26b814071e94d27aa5b23a8548d69c45221fe28@135.181.16.252:26656,72ab81b6ba22876fc7f868b58efecb05ffac9753@65.109.86.236:28656,a56c51d7a130f33ffa2965a60bee938e7a60c01f@142.132.158.4:10656,c1d2c7a810c386595e59ead21ba69555a37ac007@5.161.110.128:26656,28f14b89d10992cff60cbe98d4cd1cf84b1d2c60@88.99.214.188:26656,2b76e96658f5e5a5130bc96d63f016073579b72d@51.91.215.40:45656,11dd3e4614218bf584b6134148e2f8afae607d93@142.132.231.118:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
