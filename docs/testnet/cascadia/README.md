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
peers="5126c2904cf4d9ed9b2c6cd203fccbe3983229da@23.88.5.169:22656,7f61eb8869a103eac4a0ad02bd7ce1f42c0041bc@5.9.59.220:33656,6fd64f8f811c6a2988015043fda38587ca9cf263@49.12.221.223:23656,040d0b6ffefba3283b5763e26c352c7b1b232c1f@65.109.90.171:34656,db189c256eda0bb7a44a9f3739f8b646cb57c940@65.109.239.7:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,c9256e4f42a23bbdc9ea79805f497a1923a4beac@65.108.230.113:17096,10be839bd10e61383523a0b6302b3b056c51dab9@142.132.152.46:13656,3afe6df94dc385efa85aef823e038c76147e4c99@95.217.35.111:26656,e34cc8a12a5274272ff861b4fe3042e98697e500@46.17.250.108:60956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
