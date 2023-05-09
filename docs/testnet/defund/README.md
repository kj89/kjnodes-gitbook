# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: orbit-alpha-1 | **Latest Version Tag**: v0.2.6 | **Wasm**: ON

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/defund-testnet](https://explorer.kjnodes.com/defund-testnet)

## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: defund-testnet.grpc.kjnodes.com:14090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:14056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:14059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (10)
```bash
peers="6448d127ec3b31a1565603409c327699ff9c0b52@77.91.78.222:26656,c584a5f8c28c7548752fdfea6cf2942d5e10c82e@188.34.178.190:56656,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,26bdbcbfa286f443c842ed241d35fa09065d586b@161.97.128.243:34656,354485ffcd96d2c292969fae86624f754924bb8c@91.77.165.172:28656,6999cca6c55576a48d4f227b87dc904fbdb085aa@65.21.134.202:26576,e3c348467a8c88c0f65e2ca8a71875d2a384b8b4@185.16.39.19:60656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14056,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,e5178dc8675b4727af538a7a58d74090366af8fa@161.97.164.23:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
