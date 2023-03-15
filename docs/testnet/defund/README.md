# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-4 | **Latest Version Tag**: v0.2.5 | **Wasm**: ON

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)




## Chain explorer
[https://explorer.kjnodes.com/defund-testnet](https://explorer.kjnodes.com/defund-testnet)

## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: defund-testnet.grpc.kjnodes.com:40090

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

**live-peers** (9)
```bash
peers="9defab88984fb8732e3bc33dd05cac99530c6509@89.163.255.100:26656,3209ec925afead6706ac250aae88d1b85a45a2d3@167.86.85.247:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,b2d33977b8bca9790df391dd3559e65514f95c0f@194.146.13.253:26656,d941341fa0f985d853f0e044d075234776cf1df6@77.232.37.54:26656,8675cc6e69c2043a8dc0a854e769c1f135b5f272@23.88.73.158:26656,6d17e0f49bc1856c732f1d439647720ba127aab8@84.46.247.5:26656,d9516be6f5fffad9d2fa4354126c46ca5a6c9310@154.53.55.128:30656,e26206d0e39515fb07915b28e468729340eb112e@38.242.244.163:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
