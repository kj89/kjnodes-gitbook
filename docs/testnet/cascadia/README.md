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
peers="3314288924c02fd0c983ef99cf2d1d607b620b80@46.4.90.188:26656,77319825e184e924bd30c5bcd0a3dc0abf181f31@178.63.26.94:55656,e68592ac5232549203e521b7266123603cac18cc@167.172.102.140:26656,8c3848f0f610b6fb82e4861660162b2fdabe755b@185.193.66.217:26656,bce4f77a3339c033c95ae96cab73f642c4d15fd5@185.187.169.105:55656,5747b9780530d4d4d64aba5f66d61f8274050d8e@194.34.232.105:26656,e9594c22a58050f4ae6a096dc0bd63dbd1126191@95.217.57.203:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,1d61222b7b8e180aacebfd57fbd2d8ab95ebdc4c@65.109.93.152:35656,345f933bde192fdbab6493aa814345618d8ad6d9@194.163.150.104:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
