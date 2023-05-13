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

**live-peers** (9)
```bash
peers="1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14056,34b72721aa503574a0709b1859fb1da2aa12ce70@88.99.3.158:11256,dfa7af21b8c6efebe8aa6028196324f9e0540bbc@94.130.55.76:39656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,6999cca6c55576a48d4f227b87dc904fbdb085aa@65.21.134.202:26576,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,773b4e59036c6934cdd3c919fc74259aba7d8ab3@185.16.39.4:26656,0634225db2052d7b42f64d63d3d3f9edbbbb9309@65.109.104.111:56108"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
