# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.1 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:55090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:55656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:55659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (10)
```bash
peers="d1469dbfc3becdf0ec1640d6812793f6d33a6eda@5.9.121.55:41956,c626efeeac4ab24c2b182865e5c23a166236eec6@81.0.221.216:39656,d5ba7a2288ed176ae2e73d9ae3c0edffec3caed5@65.21.134.202:16756,6574f46631365f4ea87ad3591d1d7af4a4acedec@65.109.30.197:23656,1d61222b7b8e180aacebfd57fbd2d8ab95ebdc4c@65.109.93.152:35656,f2b1bcee05c1986a2cd88293337491c1bc249a9d@188.191.36.222:36656,4ab70c0ac15cccba56b55c61e1c5ba0e21b7f79a@75.119.139.88:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:55656,2256cfe6777faf34317e90c5e12e2e9072322a95@162.55.183.155:10656,3314288924c02fd0c983ef99cf2d1d607b620b80@46.4.90.188:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
