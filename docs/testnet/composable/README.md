# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/composable.png" alt=""><figcaption></figcaption></figure>

The complete infrastructure for cross-chain smart  contracts, applications, and modular functionality.

**Chain ID**: banksy-testnet-2 | **Latest Version Tag**: v2.3.3-testnet2fork | **Wasm**: ON

[Website](https://www.composable.finance) | [Discord](https://discord.gg/composable) | [Twitter](https://twitter.com/ComposableFin)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/composable-testnet](https://explorer.kjnodes.com/composable-testnet)

## Public endpoints

* api: [https://composable-testnet.api.kjnodes.com](https://composable-testnet.api.kjnodes.com)
* rpc: [https://composable-testnet.rpc.kjnodes.com](https://composable-testnet.rpc.kjnodes.com)
* grpc: composable-testnet.grpc.kjnodes.com:15990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@composable-testnet.rpc.kjnodes.com:15956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@composable-testnet.rpc.kjnodes.com:15959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/composable-testnet/addrbook.json > $HOME/.banksy/config/addrbook.json
```

**live-peers** (16)
```bash
peers="c0fad6f415a8913ff63981586c4518ebcd615d69@128.140.57.144:26656,4c1ea1da9fb0442201e79535d71f66a5e0e1e68c@51.91.30.173:3000,9ce5b6397c8f11a93242d619e0126a6164e42bc8@5.78.103.231:26656,c04a07a5feabf52ecdabe752a0a81bbb25402885@194.163.168.62:15956,c5ecf0c560b7d269dbcc184aca9636835a8c1597@195.3.220.22:12656,8553443b473e6e6a5d3403511d7c3be64904048d@85.239.234.199:26656,4ea491a39a329b2ef2d919b9e8cfdb3494bc5efe@65.109.23.237:27656,b672b0e847fd404866a9466baa59053709113222@185.188.249.46:15956,514fff92cf4e97bb4357c361f87adbfcd47f56ad@65.109.117.208:26656,a993843f2a86ecec052d94715a80b1cdb84984f1@65.21.129.95:27356,5e77d58d2b48e798541a5d6b2cb1280f4224081e@164.92.191.223:15956,c97dd69796a3f55fb00d92358ec34a8185e28212@5.9.79.121:49656,8b0a36c241f7ca4069026637bda2cae29ab91f65@34.22.241.150:2340,e8f3c2f68733638574e78e85df6e8bcfef87d839@65.108.73.88:2340,4a2d85ef407eea286bf4b810b17c83d2d68e4887@95.214.55.138:11656,c335629bf07eb8ed737f74b452f6f20ffd6f8248@129.213.100.3:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```
