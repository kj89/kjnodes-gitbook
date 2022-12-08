# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: lupulella-2 | **Latest Version Tag**: v1.2.0-alpha.7 | **Wasm**: ON

Website: [https://jackalprotocol.com](https://jackalprotocol.com)


## Public endpoints

* rpc: [https://jackal-testnet.rpc.kjnodes.com](https://jackal-testnet.rpc.kjnodes.com)
* api: [https://jackal-testnet.api.kjnodes.com](https://jackal-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@jackal-testnet.rpc.kjnodes.com:37656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@jackal-testnet.rpc.kjnodes.com:37659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/jackal-testnet/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (35)
```
peers="b549c1092e37db22576e31f19cbec4b1b3b36503@116.202.227.117:37656,09d9127972ded9e22f9f11833ed7fcfa149cf1fa@65.109.92.240:19126,9b2bbd5121265ebbf9003341e8a2e0abdbc24b67@46.228.199.8:26656,f3e70d3de1974208af04dac6fabd657ab4abf0ff@65.108.75.107:24656,0394449cab5a29f24dd4f37683d3b7622f27c0fc@65.108.206.118:61156,451622fd913f6119a67f67e65f3ab82c3fbea529@78.107.253.133:32656,a76cb9a09652ad3f62987966dda2199a0ee1bf64@65.109.90.33:17556,6c7100291f35132ac1b58ff7c6d05b4ce75512b7@65.108.70.119:36156,a0f726a3dffb45d9cbde0913701bd757fcd7e434@157.90.2.254:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:37656,f02bbeb265ead3acc3de4d07f8cbe68d8679f002@65.109.92.148:60856,3c6d856a429224201d78c7f28026874d10a27f57@5.75.227.78:26656,84af58201840781a0a62449d1dcdb0ad0cf5bdb3@91.223.3.144:26356,6c6c7f370febd64447770da8aec0b9d359d61565@65.109.70.23:17556,fabb22d283df1698de657c2bf4084892362136d6@65.21.232.149:26656,5eedbfbe64b942f4ab54db3842acf3bfab034c24@161.97.74.88:46656,2ededbdbd98580e22ae8c3676e37b6e1fc1d987b@142.132.248.253:23656,372111fd8c3c11a57cd34db58b2bdd8d2b6e5005@172.104.19.93:26656,bb36af02fd6e50f3bedbc58b3589bdc203d896fc@103.19.25.157:26656,80420ad774e622bda8e1dfa9b80da11eee7eed1f@144.126.140.252:29656,9a2c091798681f89b11f8eea370bf9c6284437c5@167.86.115.183:26656,d466ed1bb4f49df46ea148c3f2e8e7e65d9268ee@89.117.48.173:2516,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.57:26906,3d3408f7768441344a7cf8c3b313f9309930464d@95.111.225.137:39656,fad8061d59f269330d1545cea615d7ef3ff7bb44@209.34.205.57:26656,cecc087977336da1e9ccd2c50097cd9e7d5e1874@141.95.33.39:26656,84f520678ef59ea02f942fa6323ec562ca5a3249@45.79.161.178:26656,0e3058446ee9b1ad449b5d3a60d5c4f92dd3785c@65.109.30.12:56656,1b191fb9ef837dec648136097f94925a15dd85ab@213.170.135.20:26516,27238e2f804bf28a14c186a2e0f0ceaae0d2588f@176.9.98.24:30566,c28ae12dc190b2abfc578f8ed2fea90fa5ff3b1d@65.108.134.208:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@46.4.53.94:30567,b26f63f307ca8e80033cbc618f7577e5be7f0c1a@95.217.118.96:27363,4ea723e652f11433734ae2aa6f364ef0510d6636@16.163.74.176:26626,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:17556"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
