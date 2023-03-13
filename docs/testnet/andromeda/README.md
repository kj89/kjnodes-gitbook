# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)




## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: [https://andromeda-testnet.grpc.kjnodes.com](https://andromeda-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:47656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:47659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (11)
```bash
peers="4cd929e58c35970289659e402a582115671baaee@65.109.106.91:25656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,e2efe3e1d7e0ed2e5b6a1b384c47f745e9f205ac@65.108.141.109:31656,50ca8e25cf1c5a83aa4c79bb1eabfe88b20eb367@65.108.199.120:61356,4d4ef8f6ff2f1ac8ba5e102e858f6ecbd0d3dda1@31.220.84.3:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,f51b215535e43428b7122c3d3ebbb4ab20c1b808@185.9.144.138:26656,086dd26d09ee6ff66307555cb9a25e0df76f377f@65.108.199.206:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
