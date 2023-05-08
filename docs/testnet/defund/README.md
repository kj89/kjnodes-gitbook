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
peers="18921a27facf3760d59147e4ae176b1bdf226346@195.201.237.172:18656,354485ffcd96d2c292969fae86624f754924bb8c@91.77.165.172:28656,0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:60656,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,93153d3b1e9178f44bbbddf809a8cf7177715c03@37.221.71.67:45656,bc934501cffc27940d96e7775b6b8ae5122604ab@185.185.80.195:28656,5c9a300d730e641ede5ab7125a3e455d93ab939a@65.109.50.106:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
