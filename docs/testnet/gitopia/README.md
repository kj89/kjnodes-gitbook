# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (35)
```bash
peers="4977214dacb3713797653c1bc07b5982bcc91649@142.132.253.112:51656,9385d79528cabb5f855a02dba8c88a2d430e824a@164.68.124.151:26656,31099d763305ead833b84c28b142ecbfd3628a64@85.190.246.250:41656,3b0956b482f89b361dd350f1c6b3743096897446@65.108.124.219:35656,182a0faf787f0f62ac2af8975d951ab94573d7d2@194.195.87.52:41656,53b421af01f3260e949d6a9c2dc09e3b1dbf9fb6@109.205.181.30:41656,3727a897b2255c8a2872223af6eb3b9a36d97829@38.242.134.10:10656,12f6b84a23b054a6591c647c2a4456c40af65cce@5.9.147.22:24656,ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,a4b24424b94edf6e2b36389b550d5648946535be@178.62.206.89:26656,921348b18868c83bfc5375fc9860bb28aaaf0d0e@38.242.238.229:26656,591318ade07c267271bb27790acec9e80dc1ce14@65.21.105.9:26656,798cf016b5150592badc8257402312fc50b7361d@65.108.45.200:26878,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,15bb9edc16710d321163e7ef8b9a44959dd7e657@65.108.126.46:30656,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,4ef3c9bf8e304b6d7f557ecc0c255eeb16ba9518@65.108.235.107:41656,edae8278cef6113e38af80504fb83cbf5eb0f023@165.232.129.242:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,5c2c2b27e1824097d4f5dc7a581a8d615923e76f@185.252.235.110:41656,292c099fc654a1331d3b62a1b939f867b62ef434@45.85.147.242:656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,2f0484f05aa2d58d91aa21ea7cb9ce81c2e207ea@85.239.240.187:26656,04a4a968f62223ba4a4c498551e89cb8408008be@149.102.152.103:41656,fea7c372588898f7ea3a04373c52a30712b3c279@185.239.209.56:656,0eb70bf5e2403694109f9bba184570074c2dfdd5@38.242.235.255:26656,a6f4fd8efe8a575a15e25652ecebce3fa1ed62a0@213.239.217.52:35656,35c829910f80387ee825da9fb69efbcbf8e2149e@164.68.118.227:26656,74a4bbfbf4d1ca9852d10f3a97e4d012c62aec9e@146.190.102.111:41656,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,5b599e2470b01f8afa88448899f436130fb2e2fd@146.190.112.167:26656,e9e671e22d794a4f80e32133905c83585b057a5d@86.48.3.0:26656,4ec16520a171af24269ddb7aa57f555a455bc76d@95.111.247.144:26656,407eb21b784f1dc4e9902cb812b65eec760c6a19@185.193.66.67:656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
