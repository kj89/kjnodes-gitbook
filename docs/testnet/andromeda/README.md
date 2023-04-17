# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:47090

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

**live-peers** (29)
```bash
peers="f58c0d432b28ebefb7573ab23cb394e67098c347@209.126.81.240:26636,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.12.196:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,91fde61878d704917f882694b271b67a38865ddc@149.102.142.94:26656,8870aca1936673bb2068ed07fcadc6c46d3ec3a1@146.190.83.6:22656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,7f32e615c80cefdd6b229cba300ef9a94287f3f3@178.250.243.84:26656,7469fd307adba5d8e782908ee01f080f3e554c48@185.154.13.19:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,24971494b3a2045d26b111c85e1ea6baf15fece3@89.169.46.109:26656,20248068f368f5d1eda74646d2bfd1fcdaffb3e1@89.58.59.75:60656,b68b237dd3ea878f50dc39a684414c92e1f0ff1e@45.82.176.72:26656,7c9e768cdaa68d5c27b49797284acbd9d0dd9716@79.137.248.65:26656,717066f5726fb3cd7096f84911c7c8bfe5953e62@81.68.158.68:26656,cdffce82a5f9f646f3e8e1cf66249b490303c431@47.5.80.5:26646,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,e8f8c97c65b3e65797eca3489de7c1682e85d4df@78.25.143.46:47656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,155b0aea2daadbb77e9eb1fbb235d2d81f7467c9@104.248.135.127:47656,df7cf95427701d6d00797042fb8548a7f8eeeb6e@172.104.159.69:55716"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
