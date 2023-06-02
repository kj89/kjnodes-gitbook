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
peers="e6e3fbc13c1903ac758ce7c6fa180312b89af2e8@142.132.248.253:25656,288b101225b97a3b4c7e642e70bf8bcde962c247@185.215.164.114:26656,956e1b99ceef18f53b12ec7a0db97c350a7457a7@5.161.81.115:26656,04381c060e945c9c85b31b585483f0570f36ba7c@84.54.23.199:18656,bce4f77a3339c033c95ae96cab73f642c4d15fd5@185.187.169.105:55656,e4f58a1478a79cdd43564a851f2398f657050aa8@135.181.250.24:26656,d5ba7a2288ed176ae2e73d9ae3c0edffec3caed5@65.21.134.202:16756,47058eb9ee90cfb0b994a4a82767d3844934ee39@65.108.41.155:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,45d9fba9830260e6ee302ab3b3802f354aa3e5d8@65.109.69.240:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
