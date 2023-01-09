# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

The Business Grade Multi-Chain NFT Infrastructure for Web 3.0

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.4 | **Wasm**: OFF

[Website](https://uptick.network) | [Discord](https://discord.gg/UzeHS7fu5H) | [Twitter](https://twitter.com/uptickproject)


## Public endpoints

* rpc: [https://uptick-testnet.rpc.kjnodes.com](https://uptick-testnet.rpc.kjnodes.com)
* api: [https://uptick-testnet.api.kjnodes.com](https://uptick-testnet.api.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@uptick-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@uptick-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/uptick-testnet/addrbook.json > $HOME/.uptickd/config/addrbook.json
```

**live-peers** (19)
```bash
peers="b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666,eb5a3112a64944e2bd701ff8aa99ab95209c6310@185.198.27.110:26656,b1f4cbece3a83ea55ba28a50281eaa3af9119cd4@65.21.129.95:21256,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,6b5375296e81501b0db0a34a7a04f39520400214@65.108.45.200:27565,7a1f08486cd519270b3aeab7c6c4abf2cc07d22b@46.17.250.145:60856,b9e0210809b9dfc9cd299c6e83116d7fa45c6e27@65.109.68.93:46656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@94.23.207.45:30556,3cffe20d473b0bd4451d330da8b741b5d42dcb44@65.21.131.215:26666,75aa14851ff12bd4825fe5679958dc278086e2b9@95.216.14.72:34656,3666c65e99775b8149396fd5c781dec6a29fb13b@75.119.144.48:31656,f06b6a57001440bf3507ba2f09a3010f6d50080b@135.181.133.37:29656,12fe5ed38770b4bb59c59e183ec1161aebda2a4e@185.173.38.18:26656,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656,5368bc0c12a7bfd9d69ba192b06f2be97d28e7ef@185.239.209.56:31656,db09e85b73c4be1cab07f41422912ccad2aa5744@185.198.27.109:15656,2763c95b0c9b0b31c312b06d6ae6887968fb9830@194.163.154.224:26656,0afb5ce897e69eec34fb32bf87f4a2f93f79e0b3@65.109.65.210:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
