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
peers="7d63f71ab6356940c607d9d748262b5505b604b0@49.12.42.105:26656,494570d1973bfe4a4989bd7773d8607433a5ba21@89.58.45.204:60556,6e8c7e7e12c03843eb4090a8d8f26bcee487da37@194.163.134.39:26656,48a9d7407149515b40206aedeb489ea82518e839@5.189.185.27:18656,7a9cd31ca48252a741ef0689bc35b751bffd555c@89.117.49.164:26656,e214c682fdaa0d692b564d1d0f4f20f24e9c0cf4@38.242.147.205:18656,345f933bde192fdbab6493aa814345618d8ad6d9@194.163.150.104:26656,956e1b99ceef18f53b12ec7a0db97c350a7457a7@5.161.81.115:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,10be839bd10e61383523a0b6302b3b056c51dab9@142.132.152.46:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
