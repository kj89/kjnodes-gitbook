# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibirufi) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:39090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (26)
```bash
peers="9396be2fcf4f271496dffb8cd034d5a17e39dbcc@216.250.122.228:39656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,7d3867934f0664832f782e3579e30686b069c473@109.123.250.109:26656,de5eef4a640ca1c05e0f4b5102ace1e531c88478@38.242.154.181:26656,23a7f6ab77328d3459418e71dd284ad5a832624f@109.205.181.113:26656,cf13f41c223c6e47e581f6ae8ec7c554218de8fc@207.244.251.201:26656,11c7655bc96c229a3d18ca3bbe7d8944ce645aab@89.117.59.191:26656,041c19c1a4d728f5440600a95a3ac3cca189f75f@217.76.60.108:26656,6b69faf2cd1287de0c12e04aefcde72b6578ce40@82.208.21.249:26656,481fcddc51ad2695ef829cd8449d64b7988895db@164.92.250.88:26656,db1deb2f4d23eb91da1d10e86562d84aaa0f9a0e@5.75.239.226:26656,066fc9b23f2992505af5948d65078a422e2bd562@31.220.88.153:26656,c414545b963134299a3c64a7d6386c9c4f7bd417@93.183.208.88:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,3db2fea3bb460cf3668cbc328433e39d030f565a@109.123.243.101:26656,24b9df9d8b731fe559a749a76d7466c6646c2d23@65.21.200.124:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,ac74cb4cc17470f39a575699d4979317315cacac@185.196.20.6:26656,aa999ecb4e74d0b95465638670cd6fddc9c1f544@65.109.89.37:26656,385e57b19ab9d142b27bd0b4db3d8d84c83947e6@77.120.115.135:39656,b03b5dd5f69c63ed1acda17074f424c49af84947@84.46.242.180:39656,2fe037c0e7a8f3da20ef50f20712b55fd52a9b8b@144.91.110.211:29656,1532fb485391af0fb7b06cc089f6d71dad196c77@31.220.94.106:39656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,5c052c78ab48d0b26098574ba8b04e039209769a@95.217.1.96:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
