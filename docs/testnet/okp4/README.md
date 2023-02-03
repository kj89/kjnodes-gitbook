# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/okp4.png" width="150" alt=""><figcaption></figcaption></figure>

OKP4 is a revolutionary public blockchain protocol where communities are incentivized to  share data and services confidently. To maximize value from data, it needs to be processed  by complex algorithms and pooled with other datasets, to create valuable knowledge.

**Chain ID**: okp4-nemeton-1 | **Latest Version Tag**: v3.0.0 | **Wasm**: OFF

[Website](https://okp4.network) | [Discord](https://discord.gg/okp4) | [Twitter](https://twitter.com/OKP4_Protocol)




## Chain explorer
[https://explorer.kjnodes.com/okp4-testnet](https://explorer.kjnodes.com/okp4-testnet)

## Public endpoints

* api: [https://okp4-testnet.api.kjnodes.com](https://okp4-testnet.api.kjnodes.com)
* rpc: [https://okp4-testnet.rpc.kjnodes.com](https://okp4-testnet.rpc.kjnodes.com)
* grpc: [https://okp4-testnet.grpc.kjnodes.com](https://okp4-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@okp4-testnet.rpc.kjnodes.com:36656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@okp4-testnet.rpc.kjnodes.com:36659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/okp4-testnet/addrbook.json > $HOME/.okp4d/config/addrbook.json
```

**live-peers** (28)
```bash
peers="eff365c8e0e2f99026e3dd91704d3764eb38e0a1@65.108.13.212:26756,82bb185819e5cf2bb6a9896447672efca27f28cb@65.109.15.202:26656,473369a53bfa8a0ac4af5a191407b30bc82e83be@74.208.94.42:14656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:36656,7dfc61d3ac9f6da7fa9f4893bc0ffa17ef8006e6@185.111.159.139:36656,99f6675049e22a0216af0e2447e7a4c5021874cd@142.132.132.200:28656,269d246537499d05698c183497c4263e899036a4@65.108.9.164:35656,ba469aac96159dbb49844406423180618d267007@65.108.120.21:26113,cf5e82486c4568c29a20719a68210523826ceb00@65.108.229.102:26651,cc8bc81fea49a6a412992bb3e2c3f211d9e675c8@88.99.161.162:21656,f17338ec41b1b68b07063984feb407d9038cf78b@65.108.142.47:26616,26114bc5cb42ef90be2aba5b4b6d82bab7a60c31@185.255.131.17:26656,8cdeb85dada114c959c36bb59ce258c65ae3a09c@88.198.242.163:36656,8577873589dc7ecb9f2e32f79fe51ef7f57e40a3@65.109.161.143:26656,b0b56d944cf1cc569a1e77e0923e075bad94d755@141.95.145.41:28656,d1a0ff9bd7ea1ebd06bc7158f3523f5e557328be@163.172.131.169:26656,052e10ce23cce3249f61853e2ca6a63102b7bddb@5.161.97.198:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:26996,2f6d5a319ebee0201dff4a0e3b7526d0863a4d32@65.109.85.225:6070,d4305fcb7b20dc96481a6ae6ae84f281f3413a4e@65.109.37.58:13656,9a1e456bebf152b65c2087896779e259633ecbef@157.90.34.111:26656,2c6b5af41689145abb85f95cb49131ae9e193142@217.13.223.167:61356,ffbd1adeb58928c3f400fab23c84c3c73badd7fa@65.108.226.44:29656,7e5fc5ab113d21777cace307d672a95b16a8f2ba@145.239.47.218:26656,09f116943144c71608d98d78c2d89de82855e8a7@65.109.19.173:51656,e1635bec0e5a14dbbf1a41557714632627729ff9@195.201.16.157:36656,874373b78d2cd50e716aa464bf407581d9305655@94.250.201.130:27656,9755cab2585a2794453a5b396ef13b893393366f@65.108.212.224:46673"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.okp4d/config/config.toml
```
