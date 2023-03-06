# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" width="150" alt=""><figcaption></figcaption></figure>

Ojo is a decentralized security-first oracle network built  to support the Cosmos Ecosystem. Ojo will source price data  from a diverse catalog of on and off-chain sources and use  advanced security mechanisms to guarantee the integrity of the data it provides.

**Chain ID**: ojo-devnet | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://ojo.network) | [Discord](https://discord.gg/fd8Yrex8nC) | [Twitter](https://twitter.com/ojo_network)




## Chain explorer
[https://explorer.kjnodes.com/ojo-testnet](https://explorer.kjnodes.com/ojo-testnet)

## Public endpoints

* api: [https://ojo-testnet.api.kjnodes.com](https://ojo-testnet.api.kjnodes.com)
* rpc: [https://ojo-testnet.rpc.kjnodes.com](https://ojo-testnet.rpc.kjnodes.com)
* grpc: [https://ojo-testnet.grpc.kjnodes.com](https://ojo-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ojo-testnet.rpc.kjnodes.com:50656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ojo-testnet.rpc.kjnodes.com:50659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ojo-testnet/addrbook.json > $HOME/.ojo/config/addrbook.json
```

**live-peers** (20)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,5af3d50dcc231884f3d3da3e3caecb0deef1dc5b@142.132.134.112:25356,62fa77951a7c8f323c0499fff716cd86932d8996@65.108.199.36:24214,9edc978fd53c8718ef0cafe62ed8ae23b4603102@136.243.103.32:36656,ac5089a8789736e2bc3eee0bf79ca04e22202bef@162.55.80.116:29656,bd35cfd5bfbea4c2a63e893860d4f9a7d880957c@213.239.217.52:45656,408ee86160af26ee7204d220498e80638f7874f4@161.97.109.47:38656,c37e444f67af17545393ad16930cd68dc7e3fd08@95.216.7.169:61156,fbeb2b37fe139399d7513219e25afd9eb8f81f4f@65.21.170.3:38656,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,e54b02d103f1fcf5189a86abe542670979d2029d@65.109.85.170:58656,9bcec17faba1b8f6583d37103f20bd9b968ac857@38.146.3.230:21656,1145755896d6a3e9df2f130cc2cbd223cdb206f0@209.145.53.163:29656,b0968b57bcb5e527230ef3cfa3f65d5f1e4647dd@35.212.224.95:26656,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,2691bb6b296b951400d871c8d0bd94a3a1cdbd52@65.109.93.152:33656,cbe534c7d012e9eb4e71a5573aee8acc1adf4bc6@65.108.41.172:28056,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,3d11a6c7a5d4b3c5752be0c252c557ed4acc2c30@167.235.57.142:36656,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
