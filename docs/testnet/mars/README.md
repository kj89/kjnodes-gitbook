# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: ares-1 | **Latest Version Tag**: v1.0.0-rc7 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)


## Chain explorer
[https://explorer.kjnodes.com/mars-testnet](https://explorer.kjnodes.com/mars-testnet)

## Public endpoints

* api: [https://mars-testnet.api.kjnodes.com](https://mars-testnet.api.kjnodes.com)
* rpc: [https://mars-testnet.rpc.kjnodes.com](https://mars-testnet.rpc.kjnodes.com)
* grpc: [https://mars-testnet.grpc.kjnodes.com](https://mars-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@mars-testnet.rpc.kjnodes.com:45656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@mars-testnet.rpc.kjnodes.com:45659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/mars-testnet/addrbook.json > $HOME/.mars/config/addrbook.json
```

**live-peers** (10)
```bash
peers="d46fb5f5e70d5417962bd237d4ec8eb50c89e042@176.9.22.117:23656,7810d82538ad81e2dde14996643f02b5b048eec9@194.163.155.84:44656,cc433ed254401c8d037f14fd7f11a4626a480d21@159.89.196.188:20656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,7f614946315d781fec92baf8cd6475fa6fea482a@65.109.92.148:61356,5dac2a64e4aea39e3704d551441938a504134e95@194.113.106.81:26656,8bb6ec79bc116c36c1271a2f5c14cd6c1e1b812f@65.109.92.240:26656,e272ef7aeb2d7ac7465f42c3acd499baf4935683@154.26.139.253:17656,bddf2a56b6783c6d79c46a07cbd707083677d4c4@135.181.183.93:33656,eae08499096faf872ec686c0b5d66a7ad5ad510b@159.223.69.75:20656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
