# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:14790

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:14756
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:14759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (10)
```bash
peers="a537cc2879fc79401f6834aa6483fbb1dee18ef0@137.184.44.33:20156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,b97375574f263a2a97e6646b99f6ea444306758c@93.170.47.119:26656,6aaf94803e3f387a3ee08b731890e6914e1e3419@65.108.233.102:30656,d78df88bc4a487c140e466a23f549ed90e7ebfb6@161.97.152.157:27656,1b88dc10b14e01ef05a6c0721ce0cdd884746327@162.55.50.101:26656,537e0302400604f7dd1b8e49c5660da311066610@199.175.98.104:26656,6ef441d08cdb54b9f058884509ec65349976d73d@178.172.212.167:26656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
