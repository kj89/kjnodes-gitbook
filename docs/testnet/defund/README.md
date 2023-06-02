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
peers="8dd9f0759495b4e05ebd68a6c1600824cbed9044@65.109.48.181:28656,78ae69a09315cb1d22b260f9f526b2f609c7a215@65.108.10.22:46656,ccebeed4dae0fe100826f7c7c111d4d62c4bb546@109.123.240.111:27656,04ff1f98174b35960d8bc2d10bf0da1406f7028b@194.146.12.215:27656,ae95d629c68b76c7a0f7695b2e63e6c5464ec435@212.90.120.12:27656,4f1d96f5b8adb5bcdd59e61cb6e387ff12422a41@65.109.63.110:13656,035ff6d94b5c62d1830d71b25c259e11a679250d@38.242.158.116:27656,470e6c26996440acd257fb6cd24fd9dcd48a4f0e@149.102.136.188:27656,7a3c4079964eaca46f63f9a4ba37997ae55bee60@45.85.249.93:27656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
