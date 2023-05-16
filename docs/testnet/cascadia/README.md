# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:15590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:15556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:15559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (10)
```bash
peers="e6e3fbc13c1903ac758ce7c6fa180312b89af2e8@142.132.248.253:25656,c2ef0140958982dae978e8830003158bade2a1c6@185.249.225.63:26656,01d4ea0468873671581e3c2c56b8e6e628be7ca1@135.181.20.30:41656,5623331ab53459146cbb60efadf42899373f844b@37.27.6.70:26656,c8d5ed2ce985364551b2bf11fe78770d5caafa62@82.208.22.200:26656,af8b5486e4938c3bd9ab56fd5ee03d26857089a1@31.220.95.213:26656,4ead67f38f3163a5c849333faaaf760b6d9eda8e@185.237.253.88:26656,66b2ef37c70974c719e1f5b1e7b3ee219607a82f@161.97.128.243:27656,2e60ee40942bacb90089c285c25dc09eda918b00@135.181.217.182:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
