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
peers="e2c90e8b67e19ceee4b177ea7909dbee24de7c7a@162.55.175.11:12656,10be839bd10e61383523a0b6302b3b056c51dab9@142.132.152.46:13656,146ec57e1c3c26d11369a1a76f97efa079901f90@159.69.201.172:25656,a4fa41f9104a77cbf5310e3890a64499b8e866e4@91.230.110.190:26656,2f0f98db7eb4addb2895085962c70f1fde29f80d@217.76.50.195:26656,1d61222b7b8e180aacebfd57fbd2d8ab95ebdc4c@65.109.93.152:35656,3931d2ddb913c90a0df7b645c529a4804c5faef6@65.108.149.96:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,6452c82f6e479b764a23a5886855cdd67ba0d01b@84.46.247.94:26656,47058eb9ee90cfb0b994a4a82767d3844934ee39@65.108.41.155:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
