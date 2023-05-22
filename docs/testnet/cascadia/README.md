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
peers="5126c2904cf4d9ed9b2c6cd203fccbe3983229da@23.88.5.169:22656,7f61eb8869a103eac4a0ad02bd7ce1f42c0041bc@5.9.59.220:33656,6f44ab7ad9d6a4366a80c8fd8f904e6ab2f6e535@5.9.48.90:26656,10be839bd10e61383523a0b6302b3b056c51dab9@142.132.152.46:13656,e10667304e9a3ccdc8139e49f4e3fad7d1f9f454@89.117.51.248:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,67f25e7edb2fb19bd2a933f5ba7a87a01312eb90@89.117.49.52:26656,af8b5486e4938c3bd9ab56fd5ee03d26857089a1@31.220.95.213:26656,a8157f96618f0febc42c4e337cd1c42e3958d7ef@38.242.213.35:18656,367d2c06fb155438b7dd6c451973e68ec0c5ac30@185.218.126.179:18656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
